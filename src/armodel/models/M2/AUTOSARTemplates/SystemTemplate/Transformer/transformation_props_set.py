"""TransformationPropsSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 782)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)


class TransformationPropsSet(ARElement):
    """AUTOSAR TransformationPropsSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    transformation_props_propses: list[TransformationProps]
    def __init__(self) -> None:
        """Initialize TransformationPropsSet."""
        super().__init__()
        self.transformation_props_propses: list[TransformationProps] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "TransformationPropsSet":
        """Deserialize XML element to TransformationPropsSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TransformationPropsSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TransformationPropsSet, cls).deserialize(element)

        # Parse transformation_props_propses (list from container "TRANSFORMATION-PROPS-PROPSES")
        obj.transformation_props_propses = []
        container = ARObject._find_child_element(element, "TRANSFORMATION-PROPS-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.transformation_props_propses.append(child_value)

        return obj



class TransformationPropsSetBuilder:
    """Builder for TransformationPropsSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TransformationPropsSet = TransformationPropsSet()

    def build(self) -> TransformationPropsSet:
        """Build and return TransformationPropsSet object.

        Returns:
            TransformationPropsSet instance
        """
        # TODO: Add validation
        return self._obj
