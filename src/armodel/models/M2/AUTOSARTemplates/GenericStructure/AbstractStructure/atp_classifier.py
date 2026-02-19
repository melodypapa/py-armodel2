"""AtpClassifier AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 173)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_AbstractStructure.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from abc import ABC, abstractmethod


class AtpClassifier(Identifiable, ABC):
    """AUTOSAR AtpClassifier."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    atp_features: list[AtpFeature]
    def __init__(self) -> None:
        """Initialize AtpClassifier."""
        super().__init__()
        self.atp_features: list[AtpFeature] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "AtpClassifier":
        """Deserialize XML element to AtpClassifier object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AtpClassifier object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse atp_features (list)
        obj.atp_features = []
        for child in ARObject._find_all_child_elements(element, "ATP-FEATURES"):
            atp_features_value = ARObject._deserialize_by_tag(child, "AtpFeature")
            obj.atp_features.append(atp_features_value)

        return obj



class AtpClassifierBuilder:
    """Builder for AtpClassifier."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AtpClassifier = AtpClassifier()

    def build(self) -> AtpClassifier:
        """Build and return AtpClassifier object.

        Returns:
            AtpClassifier instance
        """
        # TODO: Add validation
        return self._obj
