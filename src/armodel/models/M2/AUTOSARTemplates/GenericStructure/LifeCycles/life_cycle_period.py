"""LifeCyclePeriod AUTOSAR element.

References:
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 392)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_GenericStructure_LifeCycles.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    date: Optional[DateTime]
    product_release: Optional[RevisionLabelString]
    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None
    @classmethod
    def deserialize(cls, element: ET.Element) -> "LifeCyclePeriod":
        """Deserialize XML element to LifeCyclePeriod object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LifeCyclePeriod object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_release
        child = ARObject._find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse date
        child = ARObject._find_child_element(element, "DATE")
        if child is not None:
            date_value = child.text
            obj.date = date_value

        # Parse product_release
        child = ARObject._find_child_element(element, "PRODUCT-RELEASE")
        if child is not None:
            product_release_value = child.text
            obj.product_release = product_release_value

        return obj



class LifeCyclePeriodBuilder:
    """Builder for LifeCyclePeriod."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LifeCyclePeriod = LifeCyclePeriod()

    def build(self) -> LifeCyclePeriod:
        """Build and return LifeCyclePeriod object.

        Returns:
            LifeCyclePeriod instance
        """
        # TODO: Add validation
        return self._obj
