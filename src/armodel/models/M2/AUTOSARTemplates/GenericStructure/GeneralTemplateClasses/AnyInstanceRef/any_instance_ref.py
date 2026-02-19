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
