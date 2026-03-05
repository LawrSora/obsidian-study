<?php
class TuringMachine {
    private $initialState;
    private $finalStates;
    private $transitions;
    private $tape;
    private $headPosition;Ы
    private $currentState;

    public function __cЫЫЫЫonstruct($initialState, $finalStates, $transitions) {
        $this->initialState = $initialState;
        $this->finalStates = $finalStates;
        $this->transitions = $transitions;
        
        // Создание остальных переменных
        $this->tape = [];
        $this->headPosition = 0;
        $this->currentState = $this->initialState;
    }
    public function run($inputString) {
        // Создаем ленту
        $this->tape = str_split($inputString);
        // Добавим пустые символы справа от ввода
        array_push($this->tape, "_");
        // Основной цикл выполнения машины
        while (!in_array($this->currentState, $this->finalStates)) {
            $currentSymbol = $this->getCurrentSymbol();
            // Проверяем наличие соответствующего правила
            if (!isset($this->transitions[$this->currentState][$currentSymbol])) {
                throw new Exception("Нет правила для состояния {$this->currentState} и символа $currentSymbol.");
            }
            // Получаем новое состояние, символ и направление перемещения головки
            [$newState, $newSymbol, $direction] = $this->transitions[$this->currentState][$currentSymbol];
            // Обновляем текущее состояние
            $this->currentState = $newState;
            // Запись нового символа на ленту
            $this->setCurrentSymbol($newSymbol);
            // Перемещение головки
            switch ($direction) {
                case 'R': 
                    $this->moveRight();
                    break;
                case 'L': 
                    $this->moveLeft();
                    break;
            }
        }
        
        // Возвращаем результирующую строку без лишних символов
        return implode('', $this->trimTape());
    }
    
    private function getCurrentSymbol() {
        return isset($this->tape[$this->headPosition]) ? $this->tape[$this->headPosition] : '_';
    }
    
    private function setCurrentSymbol($symbol) {
        $this->tape[$this->headPosition] = $symbol;
    }
    
    private function moveRight() {
        $this->headPosition++;
        
        // Если вышли за пределы ленты, добавим пустой символ
        if (!isset($this->tape[$this->headPosition])) {
            $this->tape[] = '_';
        }
    }
    
    private function moveLeft() {
        $this->headPosition--;
        
        // Если пытаемся выйти за левую границу ленты, добавим пустой символ слева
        if ($this->headPosition < 0) {
            array_unshift($this->tape, '_');
            $this->headPosition = 0;
        }
    }
    
    private function trimTape() {
        // Удаление всех ведущих и замыкающих пустых символов
        return array_filter($this->tape, function($char) {
            return $char !== '_';
        });
    }
}

// Пример использования
$initialState = 'q0';
$finalStates = ['qf'];
$transitions = [
    'q0' => [
        '0' => ['q0', '1', 'R'],
        '1' => ['q0', '0', 'R'],
        '_' => ['qf', '_', 'S'], // Завершение программы при достижении конца строки
    ]
];

$tm = new TuringMachine
($initialState, $finalStates, $transitions);
$result = $tm->run('011011');
echo $result; 
?>