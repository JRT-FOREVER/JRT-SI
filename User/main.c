#include "stm32f10x.h"
#include "pwm_output.h"
#include "USART1_Config.h"
#include <stdio.h>


//extern uint16_t time ;

int main(void)
{
	TIM3_PWM_Init();
	USART1_Config();
  NVIC_Config();
  	
	printf("准备发车");	
//	printf("\r\n 请在超级终端或者串口调试助手输入字符 \r\n");	
	
	
	
	for(;;)
	{
	
	}

	 
}

