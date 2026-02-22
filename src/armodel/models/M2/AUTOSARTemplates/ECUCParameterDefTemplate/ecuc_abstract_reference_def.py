"""EcucAbstractReferenceDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 71)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_common_attributes import (
    EcucCommonAttributes,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from abc import ABC, abstractmethod


class EcucAbstractReferenceDef(EcucCommonAttributes, ABC):
    """AUTOSAR EcucAbstractReferenceDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    with_auto: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucAbstractReferenceDef."""
        super().__init__()
        self.with_auto: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucAbstractReferenceDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucAbstractReferenceDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize with_auto
        if self.with_auto is not None:
            serialized = SerializationHelper.serialize_item(self.with_auto, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("WITH-AUTO")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucAbstractReferenceDef":
        """Deserialize XML element to EcucAbstractReferenceDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucAbstractReferenceDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucAbstractReferenceDef, cls).deserialize(element)

        # Parse with_auto
        child = SerializationHelper.find_child_element(element, "WITH-AUTO")
        if child is not None:
            with_auto_value = child.text
            obj.with_auto = with_auto_value

        return obj



