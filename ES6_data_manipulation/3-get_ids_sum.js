export default function getStudentIdsSum(arrayStudents) {
  return arrayStudents.reduce((accumulator, student) => accumulator + student.id, 0);
}
