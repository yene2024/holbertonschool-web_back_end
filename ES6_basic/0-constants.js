/* eslint-disable */
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  export function getTask() {
    return ' is okay';
  }
  
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getTask();
  
    return combination;
  }
