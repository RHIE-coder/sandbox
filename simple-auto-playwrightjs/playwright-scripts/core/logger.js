import winston from "winston";
import path from 'path'
import url from 'url'

const __filename = url.fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const options = {
  transports: [
    new winston.transports.Console({
      level: "info",
      colorize: true,
    }),
    new winston.transports.File({
      filename: path.join(__dirname, "..", "logs", "common.log"),
      level: "info",
      maxsize: 5242880,
      maxFiles: 5,
      colorize: true,
    }),
    new winston.transports.File({
      filename: path.join(__dirname, "..", "logs", "error.log"),
      level: "error",
      maxsize: 5242880,
      maxFiles: 5,
      colorize: true,
    }),
  ],
};

export default winston.createLogger(options);