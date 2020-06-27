function getUniqueTimestamp() {

var s = new Date;
uniqueTimestamp = ""  +  s.getFullYear() + s.getMonth() + s.getDay() + s.getHours() + s.getSeconds() + s.getUTCMilliseconds()

return uniqueTimestamp;

}