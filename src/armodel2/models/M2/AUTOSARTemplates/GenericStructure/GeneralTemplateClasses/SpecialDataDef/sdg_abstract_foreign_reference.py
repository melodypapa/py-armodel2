"""SdgAbstractForeignReference AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import SdgElementWithGidBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    MetaClassName,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


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
    _DESERIALIZE_DISPATCH = {
        "DEST-META-CLASS": lambda obj, elem: setattr(obj, "dest_meta_class", SerializationHelper.deserialize_by_tag(elem, "MetaClassName")),
    }


    def __init__(self) -> None:
        """Initialize SdgAbstractForeignReference."""
        super().__init__()
        self.dest_meta_class: Optional[MetaClassName] = None

    def serialize(self) -> ET.Element:
        """Serialize SdgAbstractForeignReference to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgAbstractForeignReference, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dest_meta_class
        if self.dest_meta_class is not None:
            serialized = SerializationHelper.serialize_item(self.dest_meta_class, "MetaClassName")
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

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DEST-META-CLASS":
                setattr(obj, "dest_meta_class", SerializationHelper.deserialize_by_tag(child, "MetaClassName"))

        return obj



class SdgAbstractForeignReferenceBuilder(SdgElementWithGidBuilder):
    """Builder for SdgAbstractForeignReference with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SdgAbstractForeignReference = SdgAbstractForeignReference()


    def with_dest_meta_class(self, value: Optional[MetaClassName]) -> "SdgAbstractForeignReferenceBuilder":
        """Set dest_meta_class attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'dest_meta_class' is required and cannot be None")
        self._obj.dest_meta_class = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "destMetaClass",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> SdgAbstractForeignReference:
        """Build and return the SdgAbstractForeignReference instance (abstract)."""
        raise NotImplementedError