"""MsrQueryResultTopic1 AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 345)

JSON Source: docs/json/packages/M2_MSR_Documentation_MsrQuery.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class MsrQueryResultTopic1(ARObject):
    """AUTOSAR MsrQueryResultTopic1."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize MsrQueryResultTopic1."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize MsrQueryResultTopic1 to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(MsrQueryResultTopic1, self).serialize()

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
    def deserialize(cls, element: ET.Element) -> "MsrQueryResultTopic1":
        """Deserialize XML element to MsrQueryResultTopic1 object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized MsrQueryResultTopic1 object
        """
        # Delegate to parent class to handle inherited attributes
        return super(MsrQueryResultTopic1, cls).deserialize(element)



class MsrQueryResultTopic1Builder:
    """Builder for MsrQueryResultTopic1."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: MsrQueryResultTopic1 = MsrQueryResultTopic1()

    def build(self) -> MsrQueryResultTopic1:
        """Build and return MsrQueryResultTopic1 object.

        Returns:
            MsrQueryResultTopic1 instance
        """
        # TODO: Add validation
        return self._obj
