"""Components module."""

from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.atomic_sw_component_type import (
        AtomicSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.complex_device_driver_sw_component_type import (
        ComplexDeviceDriverSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.ecu_abstraction_sw_component_type import (
        EcuAbstractionSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.pr_port_prototype import (
        PRPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
        PortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.service_sw_component_type import (
        ServiceSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.application_sw_component_type import (
        ApplicationSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.p_port_prototype import (
        PPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sw_component_type import (
        SwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.parameter_sw_component_type import (
        ParameterSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
        AbstractRequiredPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_provided_port_prototype import (
        AbstractProvidedPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.r_port_prototype import (
        RPortPrototype,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_group import (
        PortGroup,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.symbol_props import (
        SymbolProps,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.sensor_actuator_sw_component_type import (
        SensorActuatorSwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.service_proxy_sw_component_type import (
        ServiceProxySwComponentType,
    )
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.nv_block_sw_component_type import (
        NvBlockSwComponentType,
    )

__all__ = [
    "AbstractProvidedPortPrototype",
    "AbstractRequiredPortPrototype",
    "ApplicationSwComponentType",
    "AtomicSwComponentType",
    "ComplexDeviceDriverSwComponentType",
    "EcuAbstractionSwComponentType",
    "NvBlockSwComponentType",
    "PPortPrototype",
    "PRPortPrototype",
    "ParameterSwComponentType",
    "PortGroup",
    "PortPrototype",
    "RPortPrototype",
    "SensorActuatorSwComponentType",
    "ServiceProxySwComponentType",
    "ServiceSwComponentType",
    "SwComponentType",
    "SymbolProps",
]
