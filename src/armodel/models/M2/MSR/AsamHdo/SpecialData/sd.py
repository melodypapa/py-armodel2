"""Sd AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 91)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_SpecialData.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
    VerbatimStringPlain,
)


class Sd(ARObject):
    """AUTOSAR Sd."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    gid: NameToken
    value: VerbatimStringPlain
    xml_space: Optional[Any]
    def __init__(self) -> None:
        """Initialize Sd."""
        super().__init__()
        self.gid: NameToken = None
        self.value: VerbatimStringPlain = None
        self.xml_space: Optional[Any] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Sd":
        """Deserialize XML element to Sd object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Sd object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse gid
        child = ARObject._find_child_element(element, "GID")
        if child is not None:
            gid_value = child.text
            obj.gid = gid_value

        # Parse value
        child = ARObject._find_child_element(element, "VALUE")
        if child is not None:
            value_value = child.text
            obj.value = value_value

        # Parse xml_space
        child = ARObject._find_child_element(element, "XML-SPACE")
        if child is not None:
            xml_space_value = child.text
            obj.xml_space = xml_space_value

        return obj



class SdBuilder:
    """Builder for Sd."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Sd = Sd()

    def build(self) -> Sd:
        """Build and return Sd object.

        Returns:
            Sd instance
        """
        # TODO: Add validation
        return self._obj
