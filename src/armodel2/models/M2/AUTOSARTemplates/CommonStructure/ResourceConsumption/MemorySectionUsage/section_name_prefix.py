"""SectionNamePrefix AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 147)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 412)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_ResourceConsumption_MemorySectionUsage.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import (
    ImplementationProps,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation_props import ImplementationPropsBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.CommonStructure.Implementation.dependency_on_artifact import (
    DependencyOnArtifact,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SectionNamePrefix(ImplementationProps):
    """AUTOSAR SectionNamePrefix."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SECTION-NAME-PREFIX"


    implemented_in_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "IMPLEMENTED-IN-REF": lambda obj, elem: setattr(obj, "implemented_in_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SectionNamePrefix."""
        super().__init__()
        self.implemented_in_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SectionNamePrefix to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "IMPLEMENTED-IN-REF":
                setattr(obj, "implemented_in_ref", ARRef.deserialize(child))

        return obj



class SectionNamePrefixBuilder(ImplementationPropsBuilder):
    """Builder for SectionNamePrefix with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SectionNamePrefix = SectionNamePrefix()


    def with_implemented_in(self, value: Optional[DependencyOnArtifact]) -> "SectionNamePrefixBuilder":
        """Set implemented_in attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'implemented_in' is required and cannot be None")
        self._obj.implemented_in = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "implementedIn",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SectionNamePrefix:
        """Build and return the SectionNamePrefix instance with validation."""
        self._validate_instance()
        return self._obj