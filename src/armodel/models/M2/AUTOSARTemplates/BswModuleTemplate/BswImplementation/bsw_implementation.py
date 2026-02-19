"""BswImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 120)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 290)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 972)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 207)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 425)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswImplementation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_release: Optional[RevisionLabelString]
    behavior: Optional[BswInternalBehavior]
    preconfigureds: list[Any]
    recommendeds: list[Any]
    vendor_api_infix: Optional[Identifier]
    vendor_specifics: list[EcucModuleDef]
    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior: Optional[BswInternalBehavior] = None
        self.preconfigureds: list[Any] = []
        self.recommendeds: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specifics: list[EcucModuleDef] = []
    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswImplementation":
        """Deserialize XML element to BswImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswImplementation object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_release
        child = ARObject._find_child_element(element, "AR-RELEASE")
        if child is not None:
            ar_release_value = child.text
            obj.ar_release = ar_release_value

        # Parse behavior
        child = ARObject._find_child_element(element, "BEHAVIOR")
        if child is not None:
            behavior_value = ARObject._deserialize_by_tag(child, "BswInternalBehavior")
            obj.behavior = behavior_value

        # Parse preconfigureds (list)
        obj.preconfigureds = []
        for child in ARObject._find_all_child_elements(element, "PRECONFIGUREDS"):
            preconfigureds_value = child.text
            obj.preconfigureds.append(preconfigureds_value)

        # Parse recommendeds (list)
        obj.recommendeds = []
        for child in ARObject._find_all_child_elements(element, "RECOMMENDEDS"):
            recommendeds_value = child.text
            obj.recommendeds.append(recommendeds_value)

        # Parse vendor_api_infix
        child = ARObject._find_child_element(element, "VENDOR-API-INFIX")
        if child is not None:
            vendor_api_infix_value = child.text
            obj.vendor_api_infix = vendor_api_infix_value

        # Parse vendor_specifics (list)
        obj.vendor_specifics = []
        for child in ARObject._find_all_child_elements(element, "VENDOR-SPECIFICS"):
            vendor_specifics_value = ARObject._deserialize_by_tag(child, "EcucModuleDef")
            obj.vendor_specifics.append(vendor_specifics_value)

        return obj



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
