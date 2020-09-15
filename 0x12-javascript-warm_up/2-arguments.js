#!/usr/bin/node
//prints a message depending of the number of arguments passed

const args = process.argv.slice(2).length;

if (args === 0) {
	console.log('No argument');
} else if (args === 1) {
	console.log('Argument found');
} else {
	console.log('Argument found');
}
