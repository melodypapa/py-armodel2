"""Traceable AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 312)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 221)

JSON Source: docs/json/packages/M2_MSR_Documentation_BlockElements_RequirementsTracing.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.multilanguage_referrable import (
    MultilanguageReferrable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from abc import ABC, abstractmethod


class Traceable(MultilanguageReferrable, ABC):
    """AUTOSAR Traceable."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    traces: list[Traceable]
    def __init__(self) -> None:
        """Initialize Traceable."""
        super().__init__()
        self.traces: list[Traceable] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "Traceable":
        """Deserialize XML element to Traceable object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized Traceable object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(Traceable, cls).deserialize(element)

        # Parse traces (list from container "TRACES")
        obj.traces = []
        container = ARObject._find_child_element(element, "TRACES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.traces.append(child_value)

        return obj



class TraceableBuilder:
    """Builder for Traceable."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: Traceable = Traceable()

    def build(self) -> Traceable:
        """Build and return Traceable object.

        Returns:
            Traceable instance
        """
        # TODO: Add validation
        return self._obj
