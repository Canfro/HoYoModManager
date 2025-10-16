use std::{
    io::{Error, ErrorKind},
    path::PathBuf,
};

use crate::structs::mod_file::ModFile;

pub struct ModDir {
    pub path: PathBuf,
    pub name: String,
    pub mods: Vec<ModFile>,
}

impl ModDir {
    pub fn new(path: PathBuf) -> Result<Self, Error> {
        Ok(Self {
            name: path
                .file_name()
                .ok_or_else(|| Error::new(ErrorKind::NotFound, "File stem not found."))?
                .to_str()
                .ok_or_else(|| Error::new(ErrorKind::InvalidData, "Name isn't valid UTF-8."))?
                .to_string(),
            path: path,
            mods: Vec::new(),
        })
    }

    pub fn get_mods(&mut self) -> Result<(), Error> {
        for entry in self.path.read_dir()? {
            self.mods.push(ModFile::new(entry?.path())?);
        }

        Ok(())
    }
}
