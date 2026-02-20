"""AnyInstanceRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 289)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 970)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1995)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 328)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_GeneralTemplateClasses_AnyInstanceRef.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_classifier import (
    AtpClassifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)


class AnyInstanceRef(ARObject):
    """AUTOSAR AnyInstanceRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    base: AtpClassifier
    context_elements: list[AtpFeature]
    target: AtpFeature
    def __init__(self) -> None:
        """Initialize AnyInstanceRef."""
        super().__init__()
        self.base: AtpClassifier = None
        self.context_elements: list[AtpFeature] = []
        self.target: AtpFeature = None

    def serialize(self) -> ET.Element:
        """Serialize AnyInstanceRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize base
        if self.base is not None:
            serialized = ARObject._serialize_item(self.base, "AtpClassifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BASE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize context_elements (list to container "CONTEXT-ELEMENTS")
        if self.context_elements:
            wrapper = ET.Element("CONTEXT-ELEMENTS")
            for item in self.context_elements:
                serialized = ARObject._serialize_item(item, "AtpFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize target
        if self.target is not None:
            serialized = ARObject._serialize_item(self.target, "AtpFeature")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TARGET")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AnyInstanceRef":
        """Deserialize XML element to AnyInstanceRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AnyInstanceRef object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse base
        child = ARObject._find_child_element(element, "BASE")
        if child is not None:
            base_value = ARObject._deserialize_by_tag(child, "AtpClassifier")
            obj.base = base_value

        # Parse context_elements (list from container "CONTEXT-ELEMENTS")
        obj.context_elements = []
        container = ARObject._find_child_element(element, "CONTEXT-ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.context_elements.append(child_value)

        # Parse target
        child = ARObject._find_child_element(element, "TARGET")
        if child is not None:
            target_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.target = target_value

        return obj



class AnyInstanceRefBuilder:
    """Builder for AnyInstanceRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AnyInstanceRef = AnyInstanceRef()

    def build(self) -> AnyInstanceRef:
        """Build and return AnyInstanceRef object.

        Returns:
            AnyInstanceRef instance
        """
        # TODO: Add validation
        return self._obj
