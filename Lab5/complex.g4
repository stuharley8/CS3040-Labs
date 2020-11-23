/** Stuart Harley
 * Assignment 5: Complex Parser in Antlr
 */

grammar complex;

plans : (floor)+ comp;

comp : COMP (building)+;

building : BUILDING NAME WITH FLOOR floor_list | BUILDING NAME WITH FLOORS floor_list;

floor_list : LBRACKET floor_reference (COMMA floor_reference)* RBRACKET;

floor_reference : NAME;

floor : FLOOR NAME HAS ROOM room_list | FLOOR NAME HAS ROOMS room_list;

room_list : LSBRACKET room (COMMA room)* RSBRACKET;

room : NUMBER BY NUMBER;

NAME : ('A'..'Z'|'_')+;

NUMBER : ('0'..'9')+;

COMP : 'complex';

BUILDING : 'building';

WITH : 'with';

FLOOR : 'floor';

FLOORS : 'floors';

LBRACKET : '{';

RBRACKET : '}';

COMMA : ',';

HAS : 'has';

ROOM : 'room';

ROOMS : 'rooms';

LSBRACKET : '[';

RSBRACKET : ']';

BY : 'by';

WS : [ \r\n\t]+ -> channel (HIDDEN);
