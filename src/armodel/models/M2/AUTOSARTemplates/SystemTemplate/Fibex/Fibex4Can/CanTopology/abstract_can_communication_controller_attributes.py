"""AbstractCanCommunicationControllerAttributes AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 64)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Can_CanTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class AbstractCanCommunicationControllerAttributes(ARObject, ABC):
    """AUTOSAR AbstractCanCommunicationControllerAttributes."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    can_controller_fd: Optional[Any]
    can_controller_xl: Optional[Any]
    def __init__(self) -> None:
        """Initialize AbstractCanCommunicationControllerAttributes."""
        super().__init__()
        self.can_controller_fd: Optional[Any] = None
        self.can_controller_xl: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractCanCommunicationControllerAttributes":
        """Deserialize XML element to AbstractCanCommunicationControllerAttributes object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractCanCommunicationControllerAttributes object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse can_controller_fd
        child = ARObject._find_child_element(element, "CAN-CONTROLLER-FD")
        if child is not None:
            can_controller_fd_value = child.text
            obj.can_controller_fd = can_controller_fd_value

        # Parse can_controller_xl
        child = ARObject._find_child_element(element, "CAN-CONTROLLER-XL")
        if child is not None:
            can_controller_xl_value = child.text
            obj.can_controller_xl = can_controller_xl_value

        return obj



class AbstractCanCommunicationControllerAttributesBuilder:
    """Builder for AbstractCanCommunicationControllerAttributes."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractCanCommunicationControllerAttributes = AbstractCanCommunicationControllerAttributes()

    def build(self) -> AbstractCanCommunicationControllerAttributes:
        """Build and return AbstractCanCommunicationControllerAttributes object.

        Returns:
            AbstractCanCommunicationControllerAttributes instance
        """
        # TODO: Add validation
        return self._obj
