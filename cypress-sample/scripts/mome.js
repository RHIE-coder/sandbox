const { merge } = require('mochawesome-merge')

// See Params section below
const options = {
  files: [
    './report/*.json',

    // you can specify more files or globs if necessary:
    './mochawesome-report/*.json',
  ],
}

merge(options).then(report => {
  console.log(report)
})