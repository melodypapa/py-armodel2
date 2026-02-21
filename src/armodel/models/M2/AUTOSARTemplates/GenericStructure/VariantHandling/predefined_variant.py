"""PredefinedVariant AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 305)
  - AUTOSAR_FO_TPS_FeatureModelExchangeFormat.pdf (page 77)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 257)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_VariantHandling.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.VariantHandling.sw_systemconstant_value_set import (
    SwSystemconstantValueSet,
)


class PredefinedVariant(ARElement):
    """AUTOSAR PredefinedVariant."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    included_variant_refs: list[ARRef]
    post_build_variant_refs: list[Any]
    sw_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize PredefinedVariant."""
        super().__init__()
        self.included_variant_refs: list[ARRef] = []
        self.post_build_variant_refs: list[Any] = []
        self.sw_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize PredefinedVariant to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PredefinedVariant, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize included_variant_refs (list to container "INCLUDED-VARIANT-REFS")
        if self.included_variant_refs:
            wrapper = ET.Element("INCLUDED-VARIANT-REFS")
            for item in self.included_variant_refs:
                serialized = SerializationHelper.serialize_item(item, "PredefinedVariant")
                if serialized is not None:
                    child_elem = ET.Element("INCLUDED-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize post_build_variant_refs (list to container "POST-BUILD-VARIANT-REFS")
        if self.post_build_variant_refs:
            wrapper = ET.Element("POST-BUILD-VARIANT-REFS")
            for item in self.post_build_variant_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("POST-BUILD-VARIANT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize sw_refs (list to container "SW-REFS")
        if self.sw_refs:
            wrapper = ET.Element("SW-REFS")
            for item in self.sw_refs:
                serialized = SerializationHelper.serialize_item(item, "SwSystemconstantValueSet")
                if serialized is not None:
                    child_elem = ET.Element("SW-REF")
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
    def deserialize(cls, element: ET.Element) -> "PredefinedVariant":
        """Deserialize XML element to PredefinedVariant object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PredefinedVariant object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PredefinedVariant, cls).deserialize(element)

        # Parse included_variant_refs (list from container "INCLUDED-VARIANT-REFS")
        obj.included_variant_refs = []
        container = SerializationHelper.find_child_element(element, "INCLUDED-VARIANT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.included_variant_refs.append(child_value)

        # Parse post_build_variant_refs (list from container "POST-BUILD-VARIANT-REFS")
        obj.post_build_variant_refs = []
        container = SerializationHelper.find_child_element(element, "POST-BUILD-VARIANT-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.post_build_variant_refs.append(child_value)

        # Parse sw_refs (list from container "SW-REFS")
        obj.sw_refs = []
        container = SerializationHelper.find_child_element(element, "SW-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.sw_refs.append(child_value)

        return obj



class PredefinedVariantBuilder:
    """Builder for PredefinedVariant."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PredefinedVariant = PredefinedVariant()

    def build(self) -> PredefinedVariant:
        """Build and return PredefinedVariant object.

        Returns:
            PredefinedVariant instance
        """
        # TODO: Add validation
        return self._obj
