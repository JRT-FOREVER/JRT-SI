/**
  ******************************************************************************
  * @file    Project/STM32F10x_StdPeriph_Template/stm32f10x_it.c 
  * @author  MCD Application Team
  * @version V3.5.0
  * @date    08-April-2011
  * @brief   Main Interrupt Service Routines.
  *          This file provides template for all exceptions handler and 
  *          peripherals interrupt service routine.
  ******************************************************************************
  * @attention
  *
  * THE PRESENT FIRMWARE WHICH IS FOR GUIDANCE ONLY AIMS AT PROVIDING CUSTOMERS
  * WITH CODING INFORMATION REGARDING THEIR PRODUCTS IN ORDER FOR THEM TO SAVE
  * TIME. AS A RESULT, STMICROELECTRONICS SHALL NOT BE HELD LIABLE FOR ANY
  * DIRECT, INDIRECT OR CONSEQUENTI
  
  AL DAMAGES WITH RESPECT TO ANY CLAIMS ARISING
  * FROM THE CONTENT OF SUCH FIRMWARE AND/OR THE USE MADE BY CUSTOMERS OF THE
  * CODING INFORMATION CONTAINED HEREIN IN CONNECTION WITH THEIR PRODUCTS.
  *
  * <h2><center>&copy; COPYRIGHT 2011 STMicroelectronics</center></h2>
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/
#include "stm32f10x_it.h"
#include <stdio.h>
#include "pwm_output.h"
extern uint16_t time;
/** @addtogroup STM32F10x_StdPeriph_Template
  * @{
  */

/* Private typedef -----------------------------------------------------------*/
/* Private define ------------------------------------------------------------*/
/* Private macro -------------------------------------------------------------*/
/* Private variables ---------------------------------------------------------*/
/* Private function prototypes -----------------------------------------------*/
/* Private functions ---------------------------------------------------------*/

/******************************************************************************/
/*            Cortex-M3 Processor Exceptions Handlers                         */
/******************************************************************************/

/**
  * @brief  This function handles NMI exception.
  * @param  None
  * @retval None
  */
void NMI_Handler(void)
{
}

/**
  * @brief  This function handles Hard Fault exception.
  * @param  None
  * @retval None
  */
void HardFault_Handler(void)
{
  /* Go to infinite loop when Hard Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Memory Manage exception.
  * @param  None
  * @retval None
  */
void MemManage_Handler(void)
{
  /* Go to infinite loop when Memory Manage exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Bus Fault exception.
  * @param  None
  * @retval None
  */
void BusFault_Handler(void)
{
  /* Go to infinite loop when Bus Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles Usage Fault exception.
  * @param  None
  * @retval None
  */
void UsageFault_Handler(void)
{
  /* Go to infinite loop when Usage Fault exception occurs */
  while (1)
  {
  }
}

/**
  * @brief  This function handles SVCall exception.
  * @param  None
  * @retval None
  */
void SVC_Handler(void)
{
}

/**
  * @brief  This function handles Debug Monitor exception.
  * @param  None
  * @retval None
  */
void DebugMon_Handler(void)
{
}

/**
  * @brief  This function handles PendSVC exception.
  * @param  None
  * @retval None
  */
void PendSV_Handler(void)
{
}

/**
  * @brief  This function handles SysTick Handler.
  * @param  None
  * @retval None
  */
void SysTick_Handler(void)
{
}

/******************************************************************************/
/*                 STM32F10x Peripherals Interrupt Handlers                   */
/*  Add here the Interrupt Handler for the used peripheral(s) (PPP), for the  */
/*  available peripheral interrupt handler's name please refer to the startup */
/*  file (startup_stm32f10x_xx.s).                                            */
/******************************************************************************/

/**
  * @brief  This function handles PPP interrupt request.
  * @param  None
  * @retval None
  */
/*void PPP_IRQHandler(void)
{
}*/

/**
  * @}
  */ 


/******************* (C) COPYRIGHT 2011 STMicroelectronics *****END OF FILE****/

/*void EXTI15_10_IRQHandler(void)
 {
 if (EXTI_GetITStatus(EXTI_Line11) != RESET)
    {
        EXTI_ClearITPendingBit(EXTI_Line11); 
        
    }


}*/
void USART1_IRQHandler(void)
{
	uint8_t ch;
	
	
	if(USART_GetITStatus(USART1, USART_IT_RXNE) != RESET)
	{ 	
	    //ch = USART1->DR;
			ch = USART_ReceiveData(USART1);
		  
		printf("%c",ch);
		
		switch(ch)
		{
			
			case(0x11):
			{
			 time = 7200;//low speed
			break;
			}
			
			case(0x12):
			{
			 time = 4800;//normal speed
			break;
			}
			
			case(0x13):
			{
			 time = 2400	;//high speed
			break;
			}
			
/*		case(0x00):
		  {
		    printf("车已准备好，随时准备发车");
				break;
		  }			
			
*/			
		case(0x01):
			{
				TIM3_Mode_Config(500,500,0,0,time-1);//前进
				//printf("车已准备好，随时准备发车01");
				break;
			}
			
		
		case(0x02):
			{
				TIM3_Mode_Config(500,500,time,time,time-1);//后退
			  //printf("车已准备好，随时准备发车02");
				break;
			}
			
		
		case(0x03):
			{
				TIM3_Mode_Config(500,0,0,0,time-1);//左转
				//printf("车已准备好，随时准备发车03");
				break;
			}
			
		
		case(0x04):
			{
				TIM3_Mode_Config(0,500,0,0,time-1);//右转
				//printf("车已准备好，随时准备发车04");
				break;
			}
			
		
		case(0x05):
			{
				TIM3_Mode_Config(500,500,0,time,time-1);//原地左转
				//printf("车已准备好，随时准备发车05");
				break;
			}
     

		case(0x06):
			{
				TIM3_Mode_Config(500,500,time,0,time-1);//原地右转
				//printf("车已准备好，随时准备发车06");
				break;
			}			
		

		case(0x07):
			{
				TIM3_Mode_Config(0,0,0,0,time-1);//停
				//printf("车已准备好，随时准备发车07");
				break;
			}			
			
	} 
	 
}
}



 

