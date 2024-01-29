#!/usr/bin/node

const argv1 = process.argv[2];

const num = parseInt(argv1);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}

/*
#!/usr/bin/node

const inputNumber = Math.round(Number(process.argv[2]))
if (!isNaN(inputNumber)) {
    console.log('My number: ' + inputNumber);
} else {
    console.log('Not a number');
}
*/
