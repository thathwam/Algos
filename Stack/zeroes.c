int trailingZeroCountInFactorial(int n)
{
  int result = 0;
  for (int i = 5; i <= n; i *= 5)
  {
    result += n / i;
    if(i > INT_MAX / 5) // prevent integer overflow
      break;
  }
  return result;
}
