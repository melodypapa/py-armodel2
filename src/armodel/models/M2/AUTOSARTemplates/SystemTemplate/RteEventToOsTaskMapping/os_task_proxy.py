"""OsTaskProxy AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
    TimeValue,
)


class OsTaskProxy(ARElement):
    """AUTOSAR OsTaskProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "period": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # period
        "preemptability": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=OsTaskPreemptabilityEnum,
        ),  # preemptability
        "priority": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # priority
    }

    def __init__(self) -> None:
        """Initialize OsTaskProxy."""
        super().__init__()
        self.period: Optional[TimeValue] = None
        self.preemptability: Optional[OsTaskPreemptabilityEnum] = None
        self.priority: Optional[PositiveInteger] = None


class OsTaskProxyBuilder:
    """Builder for OsTaskProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: OsTaskProxy = OsTaskProxy()

    def build(self) -> OsTaskProxy:
        """Build and return OsTaskProxy object.

        Returns:
            OsTaskProxy instance
        """
        # TODO: Add validation
        return self._obj
