export default function getResponseFromAPI() {
  const myPromise = new Promise((resolve) => {
    setTimeout(() => {
      resolve('Ok');
    }, 1000);
  });
  return myPromise;
}
