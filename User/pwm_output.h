#ifndef OUTPUT_H
#define OUTPUT_H

#include "stm32f10x.h"

void TIM3_PWM_Init(void);

void TIM3_Mode_Config(u16 CCR1,u16 CCR2,u16 CCR3,u16 CCR4,u16 TIM);

extern uint16_t time ;
#endif
