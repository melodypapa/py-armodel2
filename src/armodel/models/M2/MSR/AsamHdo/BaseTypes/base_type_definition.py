"""BaseTypeDefinition AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 290)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_BaseTypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class BaseTypeDefinition(ARObject, ABC):
    """AUTOSAR BaseTypeDefinition."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize BaseTypeDefinition."""
        super().__init__()
    def serialize(self) -> ET.Element:
        """Serialize BaseTypeDefinition to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BaseTypeDefinition":
        """Deserialize XML element to BaseTypeDefinition object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BaseTypeDefinition object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class BaseTypeDefinitionBuilder:
    """Builder for BaseTypeDefinition."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BaseTypeDefinition = BaseTypeDefinition()

    def build(self) -> BaseTypeDefinition:
        """Build and return BaseTypeDefinition object.

        Returns:
            BaseTypeDefinition instance
        """
        # TODO: Add validation
        return self._obj
