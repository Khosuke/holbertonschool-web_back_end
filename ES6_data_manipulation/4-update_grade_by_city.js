export default function getStudentIdsSum(arrayStudents, city, newGrades) {
  return arrayStudents
    .filter((student) => student.location === city)
    .map((student) => {
      let grade = 'N/A';

      for (const gradeObj of newGrades) {
        if (gradeObj.studentId === student.id) {
          grade = gradeObj.grade;
          break;
        }
      }
      return { ...student, grade };
    });
}
