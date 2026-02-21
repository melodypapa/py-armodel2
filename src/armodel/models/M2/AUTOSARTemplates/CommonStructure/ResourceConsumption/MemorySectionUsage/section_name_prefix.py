"""SectionNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 147)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    implemented_in_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SectionNamePrefix to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SectionNamePrefix, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize implemented_in_ref
        if self.implemented_in_ref is not None:
            serialized = SerializationHelper.serialize_item(self.implemented_in_ref, "DependencyOnArtifact")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IMPLEMENTED-IN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SectionNamePrefix":
        """Deserialize XML element to SectionNamePrefix object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SectionNamePrefix object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SectionNamePrefix, cls).deserialize(element)

        # Parse implemented_in_ref
        child = SerializationHelper.find_child_element(element, "IMPLEMENTED-IN-REF")
        if child is not None:
            implemented_in_ref_value = ARRef.deserialize(child)
            obj.implemented_in_ref = implemented_in_ref_value

        return obj



class SectionNamePrefixBuilder:
    """Builder for SectionNamePrefix."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SectionNamePrefix = SectionNamePrefix()

    def build(self) -> SectionNamePrefix:
        """Build and return SectionNamePrefix object.

        Returns:
            SectionNamePrefix instance
        """
        # TODO: Add validation
        return self._obj
