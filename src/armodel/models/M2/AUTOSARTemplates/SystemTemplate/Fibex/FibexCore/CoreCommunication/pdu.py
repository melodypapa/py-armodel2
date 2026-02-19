"""Pdu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 303)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 340)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_FibexCore_CoreCommunication.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.FibexCore.fibex_element import (
    FibexElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    UnlimitedInteger,
)
from abc import ABC, abstractmethod


class Pdu(FibexElement, ABC):
    """AUTOSAR Pdu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    has_dynamic: Optional[Boolean]
    length: Optional[UnlimitedInteger]
    def __init__(self) -> None:
        """Initialize Pdu."""
        super().__init__()
        self.has_dynamic: Optional[Boolean] = None
        self.length: Optional[UnlimitedInteger] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Pdu":
        """Deserialize XML element to Pdu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Pdu object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse has_dynamic
        child = ARObject._find_child_element(element, "HAS-DYNAMIC")
        if child is not None:
            has_dynamic_value = child.text
            obj.has_dynamic = has_dynamic_value

        # Parse length
        child = ARObject._find_child_element(element, "LENGTH")
        if child is not None:
            length_value = child.text
            obj.length = length_value

        return obj



class PduBuilder:
    """Builder for Pdu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Pdu = Pdu()

    def build(self) -> Pdu:
        """Build and return Pdu object.

        Returns:
            Pdu instance
        """
        # TODO: Add validation
        return self._obj
