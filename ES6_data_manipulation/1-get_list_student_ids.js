export default function getListStudentIds(arrayStudent) {
  if (Array.isArray(arrayStudent)) {
    return arrayStudent.map((student) => student.id);
  }
  return [];
}
