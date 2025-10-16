use std::{
    fs::rename,
    io::{Error, ErrorKind},
    path::PathBuf,
};

pub struct ModFile {
    pub path: PathBuf,
    pub name: String,
    pub is_enabled: bool,
}

impl ModFile {
    pub fn new(path: PathBuf) -> Result<Self, Error> {
        let name: String = path
            .file_name()
            .ok_or_else(|| Error::new(ErrorKind::InvalidFilename, "Couldn't retrieve file name."))?
            .to_str()
            .ok_or_else(|| Error::new(ErrorKind::InvalidData, "Name isn't valid UTF-8."))?
            .to_string();

        Ok(Self {
            is_enabled: !&name.starts_with("DISABLED "),
            name: name,
            path: path,
        })
    }

    pub fn toggle(&mut self) -> Result<(), Error> {
        let new_name: String = if self.is_enabled {
            format!("DISABLED {}", self.name)
        } else {
            self.name.trim_start_matches("DISABLED ").to_string()
        };

        let new_path: PathBuf = self
            .path
            .parent()
            .ok_or_else(|| Error::new(ErrorKind::NotFound, "No parent directory found."))?
            .join(&new_name);

        rename(&self.path, &new_path)?;

        self.name = new_name;
        self.path = new_path;
        self.is_enabled = !self.is_enabled;

        Ok(())
    }
}
