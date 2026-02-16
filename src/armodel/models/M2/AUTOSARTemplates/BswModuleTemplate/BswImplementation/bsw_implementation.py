"""BswImplementation AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ar_release": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # arRelease
        "behavior": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=BswInternalBehavior,
        ),  # behavior
        "preconfigureds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EcucModule),
        ),  # preconfigureds
        "recommendeds": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=any (EcucModule),
        ),  # recommendeds
        "vendor_api_infix": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # vendorApiInfix
        "vendor_specifics": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="*",
            element_class=EcucModuleDef,
        ),  # vendorSpecifics
    }

    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior: Optional[BswInternalBehavior] = None
        self.preconfigureds: list[Any] = []
        self.recommendeds: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specifics: list[EcucModuleDef] = []


class BswImplementationBuilder:
    """Builder for BswImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswImplementation = BswImplementation()

    def build(self) -> BswImplementation:
        """Build and return BswImplementation object.

        Returns:
            BswImplementation instance
        """
        # TODO: Add validation
        return self._obj
