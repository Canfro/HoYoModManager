use std::{
    fs::rename,
    io::{Error, ErrorKind},
    path::PathBuf,
};

pub struct Mod {
    pub path: PathBuf,
    pub name: String,
    pub is_enabled: bool,
}

pub struct ModDir {
    pub path: PathBuf,
    pub name: String,
    pub mods: Vec<Mod>,
}

pub struct Game {
    pub path: PathBuf,
    pub name: String,
    pub mod_dirs: Vec<ModDir>,
}

impl Mod {
    pub fn new(path: PathBuf) -> Result<Self, Error> {
        let name: String = path
            .file_name()
            .ok_or_else(|| Error::new(ErrorKind::InvalidFilename, "Couldn't retrieve file name."))?
            .to_str()
            .ok_or_else(|| Error::new(ErrorKind::InvalidData, "Name isn't valid UTF-8."))?
            .to_string();

        Ok(Self {
            name: name.clone(),
            path: path,
            is_enabled: !name.starts_with("DISABLED "),
        })
    }

    pub fn toggle(&mut self) -> Result<(), Error> {
        let parent_dir: PathBuf = self
            .path
            .parent()
            .ok_or_else(|| Error::new(ErrorKind::NotFound, "No parent directory found."))?
            .to_path_buf();

        let new_name: String = if self.is_enabled {
            format!("DISABLED {}", self.name)
        } else {
            self.name.trim_start_matches("DISABLED ").to_string()
        };

        let new_path: PathBuf = parent_dir.join(&new_name);

        rename(&self.path, &new_path)?;

        self.name = new_name;
        self.path = new_path;
        self.is_enabled = !self.is_enabled;
        Ok(())
    }
}

impl ModDir {
    pub fn new(path: PathBuf) -> Result<Self, Error> {}
}

impl Game {
    pub fn new(name: String, path: PathBuf) -> Result<Self, Error> {}
}
