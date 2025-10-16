use std::{io::Error, path::PathBuf};

use crate::structs::mod_dir::ModDir;

pub struct Game {
    pub path: PathBuf,
    pub name: String,
    pub mod_dirs: Vec<ModDir>,
}

impl Game {
    pub fn new(name: String, path: PathBuf) -> Self {
        Self {
            name: name,
            path: path,
            mod_dirs: Vec::new(),
        }
    }

    pub fn get_mod_dirs(&mut self) -> Result<(), Error> {
        for entry in self.path.read_dir()? {
            self.mod_dirs.push(ModDir::new(entry?.path())?);
        }

        Ok(())
    }
}
