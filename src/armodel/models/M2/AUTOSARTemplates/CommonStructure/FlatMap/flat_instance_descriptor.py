"""FlatInstanceDescriptor AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.AbstractStructure.atp_feature import (
    AtpFeature,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.FlatMap.rte_plugin_props import (
    RtePluginProps,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class FlatInstanceDescriptor(Identifiable):
    """AUTOSAR FlatInstanceDescriptor."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "ecu_extract": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AtpFeature,
        ),  # ecuExtract
        "role": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # role
        "rte_plugin_props": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=RtePluginProps,
        ),  # rtePluginProps
        "sw_data_def": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=SwDataDefProps,
        ),  # swDataDef
        "upstream": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=AtpFeature,
        ),  # upstream
    }

    def __init__(self) -> None:
        """Initialize FlatInstanceDescriptor."""
        super().__init__()
        self.ecu_extract: Optional[AtpFeature] = None
        self.role: Optional[Identifier] = None
        self.rte_plugin_props: Optional[RtePluginProps] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.upstream: Optional[AtpFeature] = None


class FlatInstanceDescriptorBuilder:
    """Builder for FlatInstanceDescriptor."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: FlatInstanceDescriptor = FlatInstanceDescriptor()

    def build(self) -> FlatInstanceDescriptor:
        """Build and return FlatInstanceDescriptor object.

        Returns:
            FlatInstanceDescriptor instance
        """
        # TODO: Add validation
        return self._obj
