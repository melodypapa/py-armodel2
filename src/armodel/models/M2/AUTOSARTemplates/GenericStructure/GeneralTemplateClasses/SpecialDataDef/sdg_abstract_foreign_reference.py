"""SdgAbstractForeignReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MetaClassName,
)
from abc import ABC, abstractmethod


class SdgAbstractForeignReference(SdgElementWithGid, ABC):
    """AUTOSAR SdgAbstractForeignReference."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    dest_meta_class: Optional[MetaClassName]
    def __init__(self) -> None:
        """Initialize SdgAbstractForeignReference."""
        super().__init__()
        self.dest_meta_class: Optional[MetaClassName] = None
    def serialize(self) -> ET.Element:
        """Serialize SdgAbstractForeignReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgAbstractForeignReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dest_meta_class
        if self.dest_meta_class is not None:
            serialized = ARObject._serialize_item(self.dest_meta_class, "MetaClassName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DEST-META-CLASS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgAbstractForeignReference":
        """Deserialize XML element to SdgAbstractForeignReference object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgAbstractForeignReference object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgAbstractForeignReference, cls).deserialize(element)

        # Parse dest_meta_class
        child = ARObject._find_child_element(element, "DEST-META-CLASS")
        if child is not None:
            dest_meta_class_value = child.text
            obj.dest_meta_class = dest_meta_class_value

        return obj



class SdgAbstractForeignReferenceBuilder:
    """Builder for SdgAbstractForeignReference."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgAbstractForeignReference = SdgAbstractForeignReference()

    def build(self) -> SdgAbstractForeignReference:
        """Build and return SdgAbstractForeignReference object.

        Returns:
            SdgAbstractForeignReference instance
        """
        # TODO: Add validation
        return self._obj
