#!/usr/bin/node
/**
 * The first element will be `process.execPath` and the second element will be
 * the path to the JavaScript file being executed. The remaining elements will
 * be any additional command-line arguments.
 */
const len = process.argv.length;
if (len === 2) console.log('No argument');
else if (len === 3) console.log('Argument found');
else console.log('Arguments found');
