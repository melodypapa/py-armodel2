"""SenderRecCompositeTypeMapping AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 235)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_DataMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class SenderRecCompositeTypeMapping(ARObject, ABC):
    """AUTOSAR SenderRecCompositeTypeMapping."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SenderRecCompositeTypeMapping."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SenderRecCompositeTypeMapping to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SenderRecCompositeTypeMapping":
        """Deserialize XML element to SenderRecCompositeTypeMapping object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SenderRecCompositeTypeMapping object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class SenderRecCompositeTypeMappingBuilder:
    """Builder for SenderRecCompositeTypeMapping."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SenderRecCompositeTypeMapping = SenderRecCompositeTypeMapping()

    def build(self) -> SenderRecCompositeTypeMapping:
        """Build and return SenderRecCompositeTypeMapping object.

        Returns:
            SenderRecCompositeTypeMapping instance
        """
        # TODO: Add validation
        return self._obj
