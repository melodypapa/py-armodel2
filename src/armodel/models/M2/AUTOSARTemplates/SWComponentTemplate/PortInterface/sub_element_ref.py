"""SubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class SubElementRef(ARObject, ABC):
    """AUTOSAR SubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize SubElementRef."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize SubElementRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SubElementRef":
        """Deserialize XML element to SubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SubElementRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        return obj



class SubElementRefBuilder:
    """Builder for SubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SubElementRef = SubElementRef()

    def build(self) -> SubElementRef:
        """Build and return SubElementRef object.

        Returns:
            SubElementRef instance
        """
        # TODO: Add validation
        return self._obj
