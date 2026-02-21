"""AtpInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 301)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 971)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2000)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 206)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 174)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_prototype import (
    AtpPrototype,
)
from abc import ABC, abstractmethod


class AtpInstanceRef(ARObject, ABC):
    """AUTOSAR AtpInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_base_ref: ARRef
    atp_context_refs: list[ARRef]
    atp_target_ref: ARRef
    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base_ref: ARRef = None
        self.atp_context_refs: list[ARRef] = []
        self.atp_target_ref: ARRef = None

    def serialize(self) -> ET.Element:
        """Serialize AtpInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # Serialize atp_base_ref
        if self.atp_base_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_base_ref, "AtpClassifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BASE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize atp_context_refs (list to container "ATP-CONTEXT-REFS")
        if self.atp_context_refs:
            wrapper = ET.Element("ATP-CONTEXT-REFS")
            for item in self.atp_context_refs:
                serialized = SerializationHelper.serialize_item(item, "AtpPrototype")
                if serialized is not None:
                    child_elem = ET.Element("ATP-CONTEXT-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize atp_target_ref
        if self.atp_target_ref is not None:
            serialized = SerializationHelper.serialize_item(self.atp_target_ref, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-TARGET-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpInstanceRef":
        """Deserialize XML element to AtpInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse atp_base_ref
        child = SerializationHelper.find_child_element(element, "ATP-BASE-REF")
        if child is not None:
            atp_base_ref_value = ARRef.deserialize(child)
            obj.atp_base_ref = atp_base_ref_value

        # Parse atp_context_refs (list from container "ATP-CONTEXT-REFS")
        obj.atp_context_refs = []
        container = SerializationHelper.find_child_element(element, "ATP-CONTEXT-REFS")
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
                    obj.atp_context_refs.append(child_value)

        # Parse atp_target_ref
        child = SerializationHelper.find_child_element(element, "ATP-TARGET-REF")
        if child is not None:
            atp_target_ref_value = ARRef.deserialize(child)
            obj.atp_target_ref = atp_target_ref_value

        return obj



class AtpInstanceRefBuilder:
    """Builder for AtpInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpInstanceRef = AtpInstanceRef()

    def build(self) -> AtpInstanceRef:
        """Build and return AtpInstanceRef object.

        Returns:
            AtpInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
