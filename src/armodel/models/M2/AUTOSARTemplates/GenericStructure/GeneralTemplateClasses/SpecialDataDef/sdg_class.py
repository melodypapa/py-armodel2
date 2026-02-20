"""SdgClass AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 99)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 207)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_SpecialDataDef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_element_with_gid import (
    SdgElementWithGid,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    MetaClassName,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.SpecialDataDef.sdg_attribute import (
    SdgAttribute,
)
from armodel.models.M2.MSR.Documentation.BlockElements.RequirementsTracing.traceable_text import (
    TraceableText,
)


class SdgClass(SdgElementWithGid):
    """AUTOSAR SdgClass."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    attributes: list[SdgAttribute]
    caption: Optional[Boolean]
    extends_meta: Optional[MetaClassName]
    sdg_constraint_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize SdgClass."""
        super().__init__()
        self.attributes: list[SdgAttribute] = []
        self.caption: Optional[Boolean] = None
        self.extends_meta: Optional[MetaClassName] = None
        self.sdg_constraint_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize SdgClass to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SdgClass, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize attributes (list to container "ATTRIBUTES")
        if self.attributes:
            wrapper = ET.Element("ATTRIBUTES")
            for item in self.attributes:
                serialized = ARObject._serialize_item(item, "SdgAttribute")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize caption
        if self.caption is not None:
            serialized = ARObject._serialize_item(self.caption, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAPTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize extends_meta
        if self.extends_meta is not None:
            serialized = ARObject._serialize_item(self.extends_meta, "MetaClassName")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXTENDS-META")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sdg_constraint_refs (list to container "SDG-CONSTRAINT-REFS")
        if self.sdg_constraint_refs:
            wrapper = ET.Element("SDG-CONSTRAINT-REFS")
            for item in self.sdg_constraint_refs:
                serialized = ARObject._serialize_item(item, "TraceableText")
                if serialized is not None:
                    child_elem = ET.Element("SDG-CONSTRAINT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SdgClass":
        """Deserialize XML element to SdgClass object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SdgClass object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SdgClass, cls).deserialize(element)

        # Parse attributes (list from container "ATTRIBUTES")
        obj.attributes = []
        container = ARObject._find_child_element(element, "ATTRIBUTES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.attributes.append(child_value)

        # Parse caption
        child = ARObject._find_child_element(element, "CAPTION")
        if child is not None:
            caption_value = child.text
            obj.caption = caption_value

        # Parse extends_meta
        child = ARObject._find_child_element(element, "EXTENDS-META")
        if child is not None:
            extends_meta_value = child.text
            obj.extends_meta = extends_meta_value

        # Parse sdg_constraint_refs (list from container "SDG-CONSTRAINT-REFS")
        obj.sdg_constraint_refs = []
        container = ARObject._find_child_element(element, "SDG-CONSTRAINT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = ARObject._strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sdg_constraint_refs.append(child_value)

        return obj



class SdgClassBuilder:
    """Builder for SdgClass."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SdgClass = SdgClass()

    def build(self) -> SdgClass:
        """Build and return SdgClass object.

        Returns:
            SdgClass instance
        """
        # TODO: Add validation
        return self._obj
