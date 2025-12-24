const fs = require('fs');
const path = require('path');

class Parser {
  constructor(file) {
    this.file = file;
  }

  parse() {
    try {
      const data = fs.readFileSync(this.file, 'utf8');
      return JSON.parse(data);
    } catch (error) {
      if (error.code === 'ENOENT') {
        throw new Error(`File not found: ${this.file}`);
      } else if (error instanceof SyntaxError) {
        throw new Error(`Invalid JSON in file: ${this.file}`);
      } else {
        throw error;
      }
    }
  }

  isValid() {
    try {
      this.parse();
      return true;
    } catch (error) {
      return false;
    }
  }
}

module.exports = Parser;