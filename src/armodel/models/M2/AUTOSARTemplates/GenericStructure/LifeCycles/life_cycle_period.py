"""LifeCyclePeriod AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    DateTime,
    RevisionLabelString,
)


class LifeCyclePeriod(ARObject):
    """AUTOSAR LifeCyclePeriod."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_release": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # arRelease
        "date": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # date
        "product_release": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # productRelease
    }

    def __init__(self) -> None:
        """Initialize LifeCyclePeriod."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.date: Optional[DateTime] = None
        self.product_release: Optional[RevisionLabelString] = None


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
