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

    atp_base: AtpClassifier
    atp_context_refs: list[ARRef]
    atp_target: AtpFeature
    def __init__(self) -> None:
        """Initialize AtpInstanceRef."""
        super().__init__()
        self.atp_base: AtpClassifier = None
        self.atp_context_refs: list[ARRef] = []
        self.atp_target: AtpFeature = None
    def serialize(self) -> ET.Element:
        """Serialize AtpInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize atp_base
        if self.atp_base is not None:
            serialized = ARObject._serialize_item(self.atp_base, "AtpClassifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize atp_context_refs (list to container "ATP-CONTEXTS")
        if self.atp_context_refs:
            wrapper = ET.Element("ATP-CONTEXTS")
            for item in self.atp_context_refs:
                serialized = ARObject._serialize_item(item, "AtpPrototype")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize atp_target
        if self.atp_target is not None:
            serialized = ARObject._serialize_item(self.atp_target, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ATP-TARGET")
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

        # Parse atp_base
        child = ARObject._find_child_element(element, "ATP-BASE")
        if child is not None:
            atp_base_value = ARObject._deserialize_by_tag(child, "AtpClassifier")
            obj.atp_base = atp_base_value

        # Parse atp_context_refs (list from container "ATP-CONTEXTS")
        obj.atp_context_refs = []
        container = ARObject._find_child_element(element, "ATP-CONTEXTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.atp_context_refs.append(child_value)

        # Parse atp_target
        child = ARObject._find_child_element(element, "ATP-TARGET")
        if child is not None:
            atp_target_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.atp_target = atp_target_value

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
