export default function getStudentsByLocation(arrayStudents, city) {
  return arrayStudents.filter((student) => student.location === city);
}
