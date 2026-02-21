"""BusspecificNmEcu AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 675)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_NetworkManagement.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from abc import ABC, abstractmethod


class BusspecificNmEcu(ARObject, ABC):
    """AUTOSAR BusspecificNmEcu."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    def __init__(self) -> None:
        """Initialize BusspecificNmEcu."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize BusspecificNmEcu to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BusspecificNmEcu, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BusspecificNmEcu":
        """Deserialize XML element to BusspecificNmEcu object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BusspecificNmEcu object
        """
        # Delegate to parent class to handle inherited attributes
        return super(BusspecificNmEcu, cls).deserialize(element)



class BusspecificNmEcuBuilder:
    """Builder for BusspecificNmEcu."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BusspecificNmEcu = BusspecificNmEcu()

    def build(self) -> BusspecificNmEcu:
        """Build and return BusspecificNmEcu object.

        Returns:
            BusspecificNmEcu instance
        """
        # TODO: Add validation
        return self._obj
