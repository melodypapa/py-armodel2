"""BuildActionEntity AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_BuildActionManifest.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.EngineeringObject.autosar_engineering_object import (
    AutosarEngineeringObject,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.BuildActionManifest.build_action_invocator import (
    BuildActionInvocator,
)
from abc import ABC, abstractmethod


class BuildActionEntity(Identifiable, ABC):
    """AUTOSAR BuildActionEntity."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    delivery_artifacts: list[AutosarEngineeringObject]
    invocation: Optional[BuildActionInvocator]
    def __init__(self) -> None:
        """Initialize BuildActionEntity."""
        super().__init__()
        self.delivery_artifacts: list[AutosarEngineeringObject] = []
        self.invocation: Optional[BuildActionInvocator] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BuildActionEntity":
        """Deserialize XML element to BuildActionEntity object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BuildActionEntity object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BuildActionEntity, cls).deserialize(element)

        # Parse delivery_artifacts (list from container "DELIVERY-ARTIFACTS")
        obj.delivery_artifacts = []
        container = ARObject._find_child_element(element, "DELIVERY-ARTIFACTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.delivery_artifacts.append(child_value)

        # Parse invocation
        child = ARObject._find_child_element(element, "INVOCATION")
        if child is not None:
            invocation_value = ARObject._deserialize_by_tag(child, "BuildActionInvocator")
            obj.invocation = invocation_value

        return obj



class BuildActionEntityBuilder:
    """Builder for BuildActionEntity."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BuildActionEntity = BuildActionEntity()

    def build(self) -> BuildActionEntity:
        """Build and return BuildActionEntity object.

        Returns:
            BuildActionEntity instance
        """
        # TODO: Add validation
        return self._obj
