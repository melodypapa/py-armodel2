"""BswImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 120)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 290)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 207)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    behavior_ref: Optional[ARRef]
    preconfigured_refs: list[Any]
    recommended_refs: list[Any]
    vendor_api_infix: Optional[Identifier]
    vendor_specific_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior_ref: Optional[ARRef] = None
        self.preconfigured_refs: list[Any] = []
        self.recommended_refs: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specific_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize BswImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize ar_release
        if self.ar_release is not None:
            serialized = ARObject._serialize_item(self.ar_release, "RevisionLabelString")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-RELEASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize behavior_ref
        if self.behavior_ref is not None:
            serialized = ARObject._serialize_item(self.behavior_ref, "BswInternalBehavior")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BEHAVIOR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize preconfigured_refs (list to container "PRECONFIGURED-REFS")
        if self.preconfigured_refs:
            wrapper = ET.Element("PRECONFIGURED-REFS")
            for item in self.preconfigured_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("PRECONFIGURED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize recommended_refs (list to container "RECOMMENDED-REFS")
        if self.recommended_refs:
            wrapper = ET.Element("RECOMMENDED-REFS")
            for item in self.recommended_refs:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("RECOMMENDED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize vendor_api_infix
        if self.vendor_api_infix is not None:
            serialized = ARObject._serialize_item(self.vendor_api_infix, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VENDOR-API-INFIX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize vendor_specific_refs (list to container "VENDOR-SPECIFIC-REFS")
        if self.vendor_specific_refs:
            wrapper = ET.Element("VENDOR-SPECIFIC-REFS")
            for item in self.vendor_specific_refs:
                serialized = ARObject._serialize_item(item, "EcucModuleDef")
                if serialized is not None:
                    child_elem = ET.Element("VENDOR-SPECIFIC-REF")
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
    def deserialize(cls, element: ET.Element) -> "BswImplementation":
        """Deserialize XML element to BswImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswImplementation, cls).deserialize(element)

        # Parse ar_release
        child = ARObject._find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse behavior_ref
        child = ARObject._find_child_element(element, "BEHAVIOR-REF")
        if child is not None:
            behavior_ref_value = ARRef.deserialize(child)
            obj.behavior_ref = behavior_ref_value

        # Parse preconfigured_refs (list from container "PRECONFIGURED-REFS")
        obj.preconfigured_refs = []
        container = ARObject._find_child_element(element, "PRECONFIGURED-REFS")
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
                    obj.preconfigured_refs.append(child_value)

        # Parse recommended_refs (list from container "RECOMMENDED-REFS")
        obj.recommended_refs = []
        container = ARObject._find_child_element(element, "RECOMMENDED-REFS")
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
                    obj.recommended_refs.append(child_value)

        # Parse vendor_api_infix
        child = ARObject._find_child_element(element, "VENDOR-API-INFIX")
        if child is not None:
            vendor_api_infix_value = ARObject._deserialize_by_tag(child, "Identifier")
            obj.vendor_api_infix = vendor_api_infix_value

        # Parse vendor_specific_refs (list from container "VENDOR-SPECIFIC-REFS")
        obj.vendor_specific_refs = []
        container = ARObject._find_child_element(element, "VENDOR-SPECIFIC-REFS")
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
                    obj.vendor_specific_refs.append(child_value)

        return obj



class BswImplementationBuilder:
    """Builder for BswImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswImplementation = BswImplementation()

    def build(self) -> BswImplementation:
        """Build and return BswImplementation object.

        Returns:
            BswImplementation instance
        """
        # TODO: Add validation
        return self._obj
