from enum import Enum


class BalanceType(Enum):
    LL = 1
    LR = 2
    RR = 3
    RL = 4
    no_need = 5


class AVLTreeNode:
    def __init__(self, value, height, left, right):
        self.item = value
        self.height = height
        self.left = left
        self.right = right


class AVLTree:
    def __init__(self):
        self.__NIL = AVLTreeNode(None, 0, None, None)
        self.__root = self.__NIL

    def __left_roate(self, target_node: AVLTreeNode) -> AVLTreeNode:
        right_node = target_node.right
        right_left_node = target_node.right.left
        target_node.right = right_left_node
        right_node.left = target_node

        target_node.height = 1 + max(target_node.left.height, target_node.right.height)
        right_node.height = 1 + max(right_node.left.height, right_node.right.height)

        return right_node

    def __right_roate(self, target_node: AVLTreeNode) -> AVLTreeNode:
        left_node = target_node.left
        left_right_node = target_node.left.right
        target_node.left = left_right_node
        left_node.right = target_node

        target_node.height = 1 + max(target_node.left.height, target_node.right.height)
        left_node.height = 1 + max(left_node.left.height, left_node.right.height)

        return left_node

    def __need_balance(self, target_node: AVLTreeNode) -> BalanceType:
        type = BalanceType.no_need
        # 오른쪽으로 균형이 쏠린경우
        if target_node.left.height + 2 <= target_node.right.height:
            if target_node.right.height >= target_node.left.height:
                type = BalanceType.RR
            else:
                type = BalanceType.RL
        elif target_node.right.height + 2 <= target_node.left.height:
            if target_node.left.height >= target_node.right.height:
                type = BalanceType.LL
            else:
                type = BalanceType.LR

        return type

    def __avl_balance(self, target_node: AVLTreeNode, type) -> AVLTreeNode:
        if type == BalanceType.LL:
            target_node = self.__right_roate(target_node)

        elif type == BalanceType.LR:
            target_node.left = self.__left_roate(target_node.left)
            target_node = self.__right_roate(target_node)

        elif type == BalanceType.RR:
            target_node = self.__left_roate(target_node)

        elif type == BalanceType.RL:
            target_node.right = self.__right_roate(target_node.right)
            target_node - self.__left_roate(target_node)

        return target_node

    def __insert_item(self, target_node: AVLTreeNode, x):
        # 삽입 위치에 도달
        if target_node == self.__NIL:
            new_node = AVLTreeNode(x, 1, self.__NIL, self.__NIL)
            return new_node
        # 현재 값보다 삽입 값이 작을 경우 -> 왼쪽 서브트리로 이동
        elif target_node.item > x:
            target_node.left = self.__insert_item(target_node.left, x)

            # 값이 삽입되었으므로 높이를 다시 계산한다.
            target_node.height = 1 + max(
                target_node.left.height, target_node.right.height
            )
            # 현재 노드의 타입을 조사한다.
            type = self.__need_balance(target_node)

            # 밸런싱이 필요하면 밸런싱을 한다.
            if type != BalanceType.no_need:
                target_node = self.__avl_balance(target_node, type)

        else:
            target_node.right = self.__insert_item(target_node.right, x)

            # 값이 삽입되었으므로 높이를 다시 계산한다.
            target_node.height = 1 + max(
                target_node.left.height, target_node.right.height
            )

            # 현재 노드의 타입을 조사한다.
            type = self.__need_balance(target_node)

            # 밸런싱이 필요하면 밸런싱을 한다.
            if type != BalanceType.no_need:
                target_node = self.__avl_balance(target_node, type)

        return target_node

    def insert(self, x):
        self.__root = self.__insert_item(self.__root, x)

    def __search_item(self, target_node: AVLTreeNode, x):
        if target_node == self.__NIL:
            return None

        if target_node.item == x:
            return target_node
        elif target_node.item < x:
            return self.__search_item(target_node.left, x)
        else:
            return self.__search_item(target_node.right, x)

    def search(self, x):
        return self.__search_item(self.__root, x)

    def __find_minimum_node(self, target_node: AVLTreeNode):
        if target_node.left == self.__NIL:
            return target_node.right, target_node.item

        else:
            ref_node, ref_item = self.__find_minimum_node(target_node.left)

            target_node.left = ref_node
            type = self.__need_balance(target_node)
            if type != BalanceType:
                target_node = self.__avl_balance(target_node, type)

            target_node.height = 1 + max(
                target_node.left.height, target_node.right.height
            )

            return target_node, ref_item

    def __find_delete_item(self, target_node: AVLTreeNode, x):
        if target_node == self.__NIL:
            return self.__NIL

        # 삭제할 노드를 발견
        if target_node.item == x:
            # 리프노드를 삭제
            if target_node.left == self.__NIL and target_node.right == self.__NIL:
                return self.__NIL
            elif target_node.left == self.__NIL:
                return target_node.right
            elif target_node.right == self.__NIL:
                return target_node.left
            else:
                ref_node, ref_item = self.__find_minimum_node(target_node.right)
                target_node.right = ref_node
                target_node.item = ref_item

                type = self.__need_balance(target_node)
                if type != BalanceType.no_need:
                    target_node = self.__avl_balance(target_node, type)

                target_node.height = 1 + max(
                    target_node.left.height, target_node.right.height
                )

        elif target_node.item < x:
            target_node.right = self.__find_delete_item(target_node.right, x)

            type = self.__need_balance(target_node)

            if type != BalanceType.no_need:
                target_node = self.__avl_balance(target_node, type)

            target_node.height = 1 + max(
                target_node.left.height, target_node.right.height
            )

        else:
            target_node.left = self.__find_delete_item(target_node.left, x)
            if type != BalanceType.no_need:
                target_node = self.__avl_balance(target_node, type)

            target_node.height = 1 + max(
                target_node.left.height, target_node.right.height
            )

        return target_node

    def delete(self, x):
        self.__root = self.__find_delete_item(self.__root, x)

    def test(self):
        self.insert(50)
        self.insert(30)
        self.insert(70)
        self.insert(60)
        self.insert(80)
        self.insert(100)
        self.insert(160)
        self.insert(200)
        self.insert(20300)
        self.insert(30300)

        self.delete(200)
        self.delete(70)

        print(self.search(70))
