"""DataPrototypeReference AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from abc import ABC, abstractmethod


class DataPrototypeReference(ARObject, ABC):
    """AUTOSAR DataPrototypeReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    tag_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize DataPrototypeReference."""
        super().__init__()
        self.tag_id: Optional[PositiveInteger] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize tag_id
        if self.tag_id is not None:
            serialized = SerializationHelper.serialize_item(self.tag_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TAG-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeReference":
        """Deserialize XML element to DataPrototypeReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeReference, cls).deserialize(element)

        # Parse tag_id
        child = SerializationHelper.find_child_element(element, "TAG-ID")
        if child is not None:
            tag_id_value = child.text
            obj.tag_id = tag_id_value

        return obj



